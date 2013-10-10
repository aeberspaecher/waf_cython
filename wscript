#!/usr/bin/env python
#-*- coding:utf-8 -*-

top = "."
out = "build"


def options(opt):
    opt.load("compiler_c")
    opt.load("python")
    opt.load("cython")


def configure(conf):
    conf.load("compiler_c")
    conf.load("python")
    conf.load("cython")
    conf.check_python_headers()

def build(bld):
    bld(features="c cshlib pyext", source="src/foo.pyx", target="foo",
        install_path="${PYTHONDIR}/waf_cython")
