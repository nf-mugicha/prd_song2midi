#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytube import YouTube
from analize_logging import logger
import os
from pydub import AudioSegment
# import upload_s3
import asyncio


def youtube2mp3(youtube_url, line_userid):
    logger.info('youtube url: {}'.format(youtube_url))
    # S3にアップロード
    # upload_s3.sign_s3(youtube_url, 'youtube_url/{}'.format(youtube_url))
    # youtube動画を抜き出す
    yt = YouTube(youtube_url)
    logger.info(yt)
    # 動画の情報を出力
    for lis in yt.streams.all():
        logger.debug(lis)
    # get_bu_itagtodownloadメソッドででダウンロードができる
    yt2mp3 = yt.streams.get_by_itag(140).download('tmp/')
    logger.info('youtube video converted to mp4 {}'.format(yt2mp3))
    # LINEのuseridにrenameする
    input_file_path = 'tmp/{}.mp4'.format(line_userid)
    os.rename(yt2mp3, input_file_path)
    # logger.info('rename: {}'.format(os.rename(yt2mp3, 'tmp/{}.mp4'.format(line_userid))))
    logger.info('Receive mp4 file name: {}'.format(input_file_path))
    # with open(yt2mp3, 'wb') as fb:
    #     fb.write(yt2mp3)

    return input_file_path


if __name__ == "__main__":
    line_userid = 'EresMia'
    youtube_url = 'https://youtu.be/9bZkp7q19f0'
    youtube_url = "https://www.youtube.com/watch?v=8iPcqtHoR3U"
    youtube2mp3(youtube_url, line_userid)
