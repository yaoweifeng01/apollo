# ****************************************************************************
# Copyright 2018 The Apollo Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ****************************************************************************
# -*- coding: utf-8 -*-
"""Module for example of record."""

import time
import sys
import ctypes

from cyber_py import cyber
from cyber_py import parameter
# from cyber_py.proto import record_pb2

# import chatter_pb2
from google.protobuf.descriptor_pb2 import FileDescriptorProto


def print_param_info():
    print "-" * 80
    param1 = parameter.Parameter("author_name", "WanderingEarth")
    print type(param1)
    print "param ", param1.name(), "type is ", param1.type_name(), ", desc is ", param1.debug_string(), param1.as_string()
    param2 = parameter.Parameter("author_age", 5000)
    print "param ", param2.name(), "type is ", param2.type_name(), ", desc is ", param2.debug_string(), param2.as_int64()
    param3 = parameter.Parameter("author_score", 888.88)
    print "param ", param3.name(), "type is ", param3.type_name(), ", desc is ", param3.debug_string(), param3.as_double()

def print_param_srv():
    print "begint param_srv_clt", "-"*40
    param1 = parameter.Parameter("author_name", "WanderingEarth")
    param2 = parameter.Parameter("author_age", 5000)
    param3 = parameter.Parameter("author_score", 888.88)

    test_node = cyber.Node("listener")
    srv = parameter.ParameterServer(test_node)
    clt = parameter.ParameterClient(test_node, "listener")
    clt.set_parameter(param1)
    clt.set_parameter(param2)
    clt.set_parameter(param3)
    print "clt.get_parameter"
    param9 = clt.get_parameter("author_name")
    print param9.debug_string()

    param_list = clt.get_paramslist()
    print "clt param lst len is ", len(param_list)
    for param in param_list:
        print param.debug_string()

    print "server test:"
    srv.set_parameter(param1)
    param10 = srv.get_parameter("author_name")
    print param10.debug_string()
    
    param_list = srv.get_paramslist()
    print "srv param lst len is ", len(param_list)
    for param in param_list:
        print param.debug_string()


if __name__ == '__main__':
    cyber.init()
    #print_param_info()
    print_param_srv()
    cyber.shutdown()
