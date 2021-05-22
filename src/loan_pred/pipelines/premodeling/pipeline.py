from kedro.pipeline import node,Pipeline
from loan_pred.pipelines.premodeling.nodes import treat_missingval

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func= treat_missingval,
                inputs="train",
                outputs="cleantrain",
                )
        ]
    )
