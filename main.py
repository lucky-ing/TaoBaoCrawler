# -*- coding: UTF-8 -*-
# file: main.py
# author: Lucky-ing
# time: 21/11/2017
# Copyright 2017 Lucky-ing. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------

import argparse
from core import download_picture

DEFAULT_FILE_PATH= r'./image'



def parse_args():
    parser = argparse.ArgumentParser(description='TaoBao picture Download by lucky-ing. Best wish!')

    help_ = 'Download folder address, default is ./image/'
    parser.add_argument('-f', '--filepath', default=DEFAULT_FILE_PATH, help=help_)

    help_ = 'The number of download picture '
    parser.add_argument('-n', '--nummax', default='5000', help=help_)

    help_ = 'keyword for download. this arg is request.'
    parser.add_argument('-s', '--keyword', default='1', help=help_,required=True)

    args_ = parser.parse_args()
    return args_


if __name__ == "__main__":

    print('start download picture from taobao.com')
    args=parse_args()
    webcrawler=download_picture.download_picture(args)
    webcrawler.start_core()

