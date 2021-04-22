import mmcv

video = mmcv.VideoReader('videos/full_resized.mp4')
total_frames = len(video)
current_frame = 0

output = []

# iterate over all frames
for frame in video:
    for row in frame:
        for pixel in row:
            if (pixel[0] > 128):
                output.append(1)
            else:
                output.append(0)
    current_frame += 1
    print(f"{current_frame}/{total_frames}")

with open("output.txt", "w") as file:
    file.write("".join(map(str, output)))

print("Finished!")