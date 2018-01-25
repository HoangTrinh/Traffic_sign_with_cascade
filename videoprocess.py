import cv2


class VideoProcess:
    def __init__(self):
        pass

    @staticmethod
    def process_video(input_path, handle, plate, output_name,size_fluc, n_box):
        count = 0
        video = cv2.VideoCapture(input_path)
        success, image = video.read()
        if not success:
            print("Read video failed!")
            return
        handle.on_video_loaded(video, output_name)
        while success:
            handle.on_receive_frame(count, image, plate,size_fluc, n_box)
            count += 1
            success, image = video.read()
        print("Process video for " + plate + " completed!")
        handle.on_video_completed(plate)
        video.release()
