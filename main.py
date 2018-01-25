import os
import input_functions
from videoprocess import *
from videoprocesshandle import VideoProcessHandle


def run():
    config = input_functions.read_config('config.txt')
    if len(config) != 6:
        print('error from config file')
        return

    in_video = config['in_video']
    final_output_name = config['out_video']
    video_format = config['format']
    plates = config['plates']
    min_id = config['from_frame']
    max_id = config['to_frame']

    if os.path.exists('output.txt'):
        os.remove('output.txt')

    frame_ids = []
    for i in range(min_id, max_id):
        frame_ids.append(i)
    handle = VideoProcessHandle(frame_ids)

    temp_output_name = final_output_name
    videos_out = []
    for key, value in plates.items():
        VideoProcess.process_video(in_video + video_format, handle, key, temp_output_name, value[0], value[1])
        videos_out.append(temp_output_name + video_format)
        in_video = temp_output_name
        temp_output_name = temp_output_name + "_" + key

    for video in videos_out[:-2]:
        os.remove(video)

    os.rename(videos_out[-1], final_output_name + video_format)


run()
