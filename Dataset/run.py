from azureml.core import Workspace, Experiment, ScriptRunConfig
from azureml.core import Dataset,  Datastore

# get workspace
ws = Workspace.from_config()

# get datastore
# ds = Datastore(ws, "<name-of-datastore>")
ds = ws.get_default_datastore()

# upload data to datastore
ds.upload_files(["example.csv"])#, target_path='outputs', overwrite=True)

# create dataset
# dataset = Dataset.File.from_files(def_blob_store.path("<path-on-datastore>"))
dataset = Dataset.File.from_files(path = [(ds, 'example.csv')])

#  get/create experiment
exp = Experiment(ws, 'dataset')

# set up script run configuration
config = ScriptRunConfig(
    source_directory='.',
    script='script.py',
    arguments=['--data', dataset.as_named_input('example').as_mount()],
)

# submit script to AML
run = exp.submit(config)
print(run.get_portal_url()) # link to ml.azure.com
