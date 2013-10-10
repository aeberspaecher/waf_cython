Fiddling around with waf's cython tool
======================================

About
-----

Cython seems to do something insane - when compiling foo.pyx, the definitions
in foo.pxd will be used implicitly in case foo.pxd is present.

This confuses waf (and in my understanding, waf is not to blame here).

Breaking things
---------------

Uncomment the cdef line in foo.pxd after you have built the Cython extension.
As an (implicit) dependency of foo.pyx has changed, the extension should be
rebuild. However, it isn't.
