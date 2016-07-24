import os
import pandas as pd

project_dir = os.getenv("PROJECT_DIR")
env = os.getenv("CONDA_DEFAULT_ENV")
iris_csv = os.getenv("IRIS_CSV")
column_to_show = os.getenv("COLUMN_TO_SHOW")

flowers = pd.read_csv(iris_csv)

print("Showing column {}".format(column_to_show))
print(flowers[column_to_show])
print("My project directory is {} and my conda environment is {}".format(project_dir, env))
