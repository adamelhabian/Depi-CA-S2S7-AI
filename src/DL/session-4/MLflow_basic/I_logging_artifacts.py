import mlflow

mlflow.set_experiment("testing_mlflow")  # ينشئ experiment إذا لم يكن موجود

with mlflow.start_run(run_name="logging_artifacts") as run:
    with open("TESTING_MLFLOW.txt", "w") as f:
        f.write("DATA_SCIENCE")
    mlflow.log_artifact("TESTING_MLFLOW.txt", "text_files")

    print("run_id:", run.info.run_id)
    print("experiment_id:", run.info.experiment_id)