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
"""Module for init environment."""

import sys
import os
import importlib
import time
import threading
import ctypes

from google.protobuf.descriptor_pb2 import FileDescriptorProto

PY_TIMER_CB_TYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)

# init vars
CYBER_PATH = os.environ['CYBER_PATH']
CYBER_DIR = os.path.split(CYBER_PATH)[0]
sys.path.append(CYBER_PATH + "/third_party/")
sys.path.append(CYBER_PATH + "/lib/")
sys.path.append(CYBER_PATH + "/python/cyber")
sys.path.append(CYBER_PATH + "/python/cyber_py")

sys.path.append(CYBER_PATH + "/lib/python/")

sys.path.append(CYBER_DIR + "/python/")
sys.path.append(CYBER_DIR + "/cyber/")

_CYBER_PARAM = importlib.import_module('_cyber_parameter')


class Parameter(object):

    """
    Class for Parameter wrapper.
    """

    def __init__(self, name, value=None):
        '''
        '''
        if (name != None and value == None):  # support PyCapsule, how to check PyCapsule
            self.param = name
        elif (name == None and value == None):
            self.param = _CYBER_PARAM.new_PyParameter_noparam()
        elif isinstance(value, int) or isinstance(value, long):
            self.param = _CYBER_PARAM.new_PyParameter_int(name, value)
        elif isinstance(value, float):
            self.param = _CYBER_PARAM.new_PyParameter_double(name, value)
        elif isinstance(value, str):
            self.param = _CYBER_PARAM.new_PyParameter_string(name, value)
        else:
            print "type is not supported: ", type(value)

    def __del__(self):
        _CYBER_PARAM.delete_PyParameter(self.param)

    def type_name(self):
        '''
        return Parameter typename
        '''
        return _CYBER_PARAM.PyParameter_type_name(self.param)

    def descriptor(self):
        '''
        return Parameter descriptor
        '''
        return _CYBER_PARAM.PyParameter_descriptor(self.param)

    def name(self):
        '''
        return Parameter descriptor
        '''
        return _CYBER_PARAM.PyParameter_name(self.param)

    def debug_string(self):
        '''
        return Parameter debug
        '''
        return _CYBER_PARAM.PyParameter_debug_string(self.param)

    def as_string(self):
        '''
        return native value
        '''
        return _CYBER_PARAM.PyParameter_as_string(self.param)

    def as_double(self):
        '''
        return native value
        '''
        return _CYBER_PARAM.PyParameter_as_double(self.param)

    def as_int64(self):
        '''
        return native value
        '''
        return _CYBER_PARAM.PyParameter_as_int64(self.param)


class ParameterClient(object):

    """
    Class for ParameterClient wrapper.
    """

    def __init__(self, node, server_node_name):
        '''
        '''
        self.param_clt = _CYBER_PARAM.new_PyParameterClient(
            node.node, server_node_name)
        print "typeis", type(self.param_clt)

    def __del__(self):
        _CYBER_PARAM.delete_PyParameterClient(self.param_clt)

    def set_parameter(self, param):
        return _CYBER_PARAM.PyParameter_clt_set_parameter(self.param_clt, param.param)

    def get_parameter(self, param_name):
        return Parameter(_CYBER_PARAM.PyParameter_clt_get_parameter(self.param_clt, param_name))
    
    def get_paramslist(self):
        pycapsulelist = _CYBER_PARAM.PyParameter_clt_get_parameter_list(self.param_clt)
        print pycapsulelist, len(pycapsulelist)
        param_list = []
        for capsuleobj in pycapsulelist:
            param_list.append(Parameter(capsuleobj))
        return param_list

class ParameterServer(object):

    """
    Class for ParameterServer wrapper.
    """

    def __init__(self, node):
        '''
        '''
        self.param_srv = _CYBER_PARAM.new_PyParameterServer(node.node)

    def __del__(self):
        _CYBER_PARAM.delete_PyParameterServer(self.param_srv)

    def set_parameter(self, param):
        return _CYBER_PARAM.PyParameter_srv_set_parameter(self.param_srv, param.param)

    def get_parameter(self, param_name):
        return Parameter(_CYBER_PARAM.PyParameter_srv_get_parameter(self.param_srv, param_name))

    def get_paramslist(self):
        pycapsulelist = _CYBER_PARAM.PyParameter_srv_get_parameter_list(self.param_srv)
        print pycapsulelist, len(pycapsulelist)
        param_list = []
        for capsuleobj in pycapsulelist:
            param_list.append(Parameter(capsuleobj))
        return param_list