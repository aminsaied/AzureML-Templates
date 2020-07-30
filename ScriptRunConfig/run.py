from azureml.core import Workspace, Experiment, ScriptRunConfig

# get workspace
ws = Workspace.from_config()

#  get/create experiment
exp = Experiment(ws, 'script-run-config')

# set up script run configuration
config = ScriptRunConfig(
    source_directory='.',
    script='script.py',
    arguments=['--meaning', 42],
)

# submit script to AML
run = exp.submit(config)
print(run.get_portal_url()) # link to ml.azure.com
