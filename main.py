from sch import schconnection
from pipelines import sdc_first_pipeline, sdc_second_pipeline


def switch(pipeline):
    if pipeline == 'sdc_first_pipeline':
        sdc_first_pipeline.publish(sch,
                                   engine_type="data_collector",
                                   engine_id="9946e354-616b-4969-8dcc-f02a4dafe983",
                                   pipeline_name=pipeline,
                                   commit_message='MCR001')
    elif pipeline == 'sdc_second_pipeline':
        sdc_second_pipeline.publish(sch,
                                    engine_type="data_collector",
                                    engine_id="9946e354-616b-4969-8dcc-f02a4dafe983",
                                    pipeline_name=pipeline,
                                    commit_message='MCR001')


if __name__ == '__main__':
    sch = schconnection.connect()
    run_pipelines = ['sdc_first_pipeline', 'sdc_second_pipeline']
    for run_pipeline in run_pipelines:
        switch(run_pipeline)
