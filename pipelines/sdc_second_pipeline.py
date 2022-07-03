import string
from streamsets.sdk import ControlHub


def publish(sch: ControlHub,
            engine_type: string,
            engine_id: string,
            pipeline_name: string,
            commit_message: string):
    try:
        old_pipeline = sch.pipelines.get(filter_text=pipeline_name)
    except ValueError:
        print(f"{pipeline_name} doesnt exist. Creating a new pipeline")
        old_pipeline = None
    builder = sch.get_pipeline_builder(engine_type=engine_type, engine_id=engine_id)
    dev_raw_data_source = builder.add_stage('Dev Raw Data Source')
    field_order = builder.add_stage('Field Order')
    field_order.fields_to_order = ['/f1', '/f2', '/f3']
    trash = builder.add_stage('Trash')
    dev_raw_data_source >> field_order >> trash
    pipeline = builder.build(pipeline_name)
    if old_pipeline:
        pipeline.pipeline_id = old_pipeline.pipeline_id
        pipeline.commit_id = old_pipeline.commit_id
        pipeline.version = old_pipeline.version
    sch.publish_pipeline(pipeline=pipeline, commit_message=commit_message)
