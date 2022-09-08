#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Dataset Download"""

import os
from mindcv.utils.download import DownLoad


class MnistDownload(DownLoad):
    url_path = 'http://yann.lecun.com/exdb/mnist/'

    resources = [("train-images-idx3-ubyte.gz", "f68b3c2dcbeaaa9fbdd348bbdeb94873"),
                 ("train-labels-idx1-ubyte.gz", "d53e105ee54ea40749a09fcbcd1e9432"),
                 ("t10k-images-idx3-ubyte.gz", "9fb629c4189551a2d022fa330f9573f3"),
                 ("t10k-labels-idx1-ubyte.gz", "ec29112dd5afa0611ce80d1b7f02629c")]

    def __init__(self, root: str):
        super(MnistDownload, self).__init__()
        self.root = root
        self.path = root

    def download(self):
        """Download the MNIST dataset if it doesn't exists."""
        bool_list = []
        # Check whether the file exists and check value of md5.
        for url, md5 in self.resources:
            filename = os.path.splitext(url)[0]
            file_path = os.path.join(self.root, filename)
            bool_list.append(os.path.isfile(file_path))
        if all(bool_list):
            return

        # download files
        for filename, md5 in self.resources:
            url = os.path.join(self.url_path, filename)
            self.download_and_extract_archive(url,
                                              download_path=self.root,
                                              filename=filename,
                                              md5=md5,
                                              remove_finished=True)


class Cifar10Download(DownLoad):
    url = ('http://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz', 'c32a1d4ab5d03f1284b67883e8d87530')
    base_dir = 'cifar-10-batches-bin'

    resources = ['data_batch_1.bin',
                 'data_batch_2.bin',
                 'data_batch_3.bin',
                 'data_batch_4.bin',
                 'data_batch_5.bin',
                 'test_batch.bin',
                 'batches.meta.txt']

    def __init__(self, root: str):
        super(Cifar10Download, self).__init__()
        self.root = root
        self.path = os.path.join(self.root, self.base_dir)

    def download(self):
        """Download the Cifar10 dataset if it doesn't exists."""
        bool_list = []
        # Check whether the file exists and check value of md5.
        for filename in self.resources:
            file_path = os.path.join(self.root, self.base_dir, filename)
            bool_list.append(os.path.isfile(file_path))
        if all(bool_list):
            return

        # download files
        self.download_and_extract_archive(self.url[0],
                                          download_path=self.root,
                                          md5=self.url[1],
                                          remove_finished=True)


class Cifar100Download(DownLoad):
    url = ('http://www.cs.toronto.edu/~kriz/cifar-100-binary.tar.gz', '03b5dce01913d631647c71ecec9e9cb8')
    base_dir = 'cifar-100-binary'

    resources = ['train.bin',
                 'test.bin',
                 'fine_label_names.txt',
                 'coarse_label_names.txt']

    def __init__(self, root: str):
        super(Cifar100Download, self).__init__()
        self.root = root
        self.path = os.path.join(self.root, self.base_dir)

    def download(self):
        """Download the Cifar100 dataset if it doesn't exists."""
        bool_list = []
        # Check whether the file exists and check value of md5.
        for filename in self.resources:
            file_path = os.path.join(self.root, self.base_dir, filename)
            bool_list.append(os.path.isfile(file_path))
        if all(bool_list):
            return

        # download files
        self.download_and_extract_archive(self.url[0],
                                          download_path=self.root,
                                          md5=self.url[1],
                                          remove_finished=True)
