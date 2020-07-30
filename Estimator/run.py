from azureml.core import Workspace, Experiment, ComputeTarget
from azureml.train.estimator import Estimator

# get workspace
ws = Workspace.from_config()

#  get/create experiment
exp = Experiment(ws, 'estimator')

# define compute target
compute_target = ComputeTarget(ws, 'cpu1')

# set up script run configuration
config = Estimator(
    source_directory='.',
    entry_script='script.py',
    compute_target=compute_target,
    script_params={'--meaning': 42},
)

# submit script to AML
run = exp.submit(config)
print(run.get_portal_url()) # link to ml.azure.com
