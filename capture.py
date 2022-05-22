from argparse import ArgumentParser
from os import environ, makedirs
from shutil import rmtree
import subprocess


def main(dt, hour, min, rotation=None):
    """
    Example Usage:

    Python capture.py \
        --dt ${date -I} \
        --hour ${date "+%H"} \
        --min ${date "+%M"}

    """

    # take a photo
    path_head = f'{environ["HOME"]}/Pictures/bike-cam/dt={dt}/hour={hour}/min={min}'
    gcs_path = 'gs://' + path_head.replace(f'{environ["HOME"]}/Pictures/', '')
    file_path =f'{path_head}/photo.jpg'
    cam_command = f'raspistill -o {file_path}'.split()
    sync_cmd = f'gsutil -m rsync {path_head} {gcs_path}'.split()

    if rotation:
        """-rot, --rotation	: Set image rotation (0, 90, 180, or 270)"""
        cam_command.extend(['-rot', f'{rotation}'])

    # write to /path/with/dt/hour/min hive partitions
    makedirs(path_head)
    subprocess.run(cam_command)

    # gsutil sync to bike-cam bucket
    subprocess.run(sync_cmd)

    # clean up
    rmtree(path_head)



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--dt", required=True)
    parser.add_argument("--hour", required=True)
    parser.add_argument("--min", required=True)
    parser.add_argument("--rot", choices=["90", "180", "270"])

    args = parser.parse_args()

    main(args.dt, args.hour, args.min, args.rot)
