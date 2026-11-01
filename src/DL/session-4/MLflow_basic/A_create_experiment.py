import mlflow

if __name__ == "__main__":
    # create a new mlflow experiment
    # contain each different run
    experiment_id = mlflow.create_experiment(
        name="DEPI_DS",
        # store any file related to experiment
        artifact_location="testing_mlflow1_artifacts",
        tags={"env": "dev", "version": "1.0.0"},
    )

    print(experiment_id)