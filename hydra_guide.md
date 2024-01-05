# Hydra Example Guide

This example will show how to create a CLI with hydra. The code is in `hydra_example.py`.

## Table of Contents

1. [Setup CLI with Hydra](#setup-cli-with-hydra)
2. [Run a Job](#run-a-job)
3. [Logging Config](#logging-config)
4. [Re-run Jobs](#re-run-jobs)
5. [**DIY**: Other Resources](#other-resources)

## Setup CLI with Hydra

Hydra allow you to create command line interface like `argparse`, `fire`, `typer` etc. It can be combined with Pydantic validation. 

Let's see how to build a CLI with hydra.

### Create Pydantic Model for CLA
```python
class ProjectConfig(BaseConfig):
    data: DataConfig
    model: ModelConfig
```
### Setup `main` function to parse args from hydra
```python
from omegaconf import DictConfig, OmegaConf
import hydra
@hydra.main(version_base=None, config_path="config",config_name="cla")
def main(cla: DictConfig):
    pass

if __name__ == "__main__":
    main()
```
### Resolve and parse CLA as Pydantic object
```python
OmegaConf.resolve(cla)
cla = ProjectConfig(**cla)
```
### Create `config/cla.yaml` with default CLA values
see `config/cla.yaml`

## Run a job

You now can run your python file as usual, also override arguments in command line just like other CLI tools.

### See help

It should show you what are current default CLA values are.

```python
python hydra_example.py --help
```
### See hydra help

You can change config file name, config folder with `--config-name` and `--config-dir`

```python
python hydra_example.py --hydra-help
```

### Override from command line argument

You can override any argument that is in the `cla.yaml` from command line:

```python
python hydra_example.py model.max_depth=10
```

```python
python hydra_example.py model.max_depth=10 data.window=30
```

### Multirun

Hydra also supports running multiple jobs with different arguments with a single command:

```python
python hydra_example.py -m data.window=2,3
```

```python
python hydra_example.py -m data.window=2,3 model.max_depth=7,8
```

By default, Hydra runs your multi-run jobs locally and serially. Other launchers are available as plugins for launching in parallel and on different clusters.

For example, the [JobLib Launcher](https://hydra.cc/docs/plugins/joblib_launcher/) can execute the different parameter combinations in parallel on your local machine using multi-processing.

## Logging Config

With hydra, it is easy to setup logging handlers, formatters.

### Color Logging

Colorlog plugin is supported: https://hydra.cc/docs/plugins/colorlog/

You can define it in `cla.yaml`:

```
defaults:
  - override hydra/hydra_logging: colorlog
  - override hydra/job_logging: colorlog
```
### Custom Logging

You can also define your custom logging settings, see an example in `hydra/job_logging/logging_config.yaml`.

### Set Verbose

Set `hydra.verbose=True` to also see debug logging messages. Default is `False`.

```python
python hydra_example.py hydra.verbose=True
```
Disable logging:

```python
python hydra_example.py hydra/job_logging=disabled
```


## Re-run Jobs

Hydra save detailed configurations for each run, and it is also possible to re-run a previous run!

### Runs History

Hydra saves all your runs, its logs, configs, overrides etc. You can find them under `outputs` or `multirun`. Remember to `.gitignore` them.

### Re-run a Job

First you need to pickle the run config by adding callback configuration. See an example in `config/hydra/callbacks/experiment.yaml`.

Then directly re-run the job from that `config.pickle`, notice it will append logs in the original log file.

```python
python hydra_example.py --experimental-rerun outputs/your-desired-previous-run/.hydra/config.pickle
```


## Other Resources

There are a lot more in Hydra to be explored! It's time to try it yourself ;)

### Custom `--help` message

For hydra, it is easy to re-write the info in `--help`, so that you could give user more guidance for your CLI.

See the docs for more:

https://hydra.cc/docs/configure_hydra/app_help/#internaldocs-banner

### Auto-tab completion

Hydra also possible to do auto completion on overrides arguments, but you need to install some other dependencies.

See the docs for more:

https://hydra.cc/docs/tutorials/basic/running_your_app/tab_completion/#internaldocs-banner

### Hydra with MLFlow

Hydra can be nicely integrated with MLFlow.

See a nice data science project example here:
https://github.com/udacity/cd0581-building-a-reproducible-model-workflow-exercises/tree/main/lesson-5-final-pipeline-release-and-deploy/exercises/exercise_14/solution

### Hydra with Optuna

Hydra can be integrated with Optuna for parameters sweeping.

See the docs for more:

https://hydra.cc/docs/plugins/optuna_sweeper/