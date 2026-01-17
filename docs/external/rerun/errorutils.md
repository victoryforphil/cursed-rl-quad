---
source: https://ref.rerun.io/docs/python/stable/common/errorutils
title: ErrorUtils
---

# ErrorUtils



### rerun.error_utils



#### classRerunIncompatibleDependencyVersionError



Bases: `ImportError`



Raised when a dependency has an incompatible version.



#### classRerunMissingDependencyError



Bases: `ImportError`



Raised when an optional dependency is not installed.



#### classRerunWarning



Bases: `Warning`



A custom warning class that we use to identify warnings that are emitted by the Rerun SDK itself.



#### classcatch_and_log_exceptions



A hybrid decorator / context-manager.



We can add this to any function or scope where we want to catch and log
exceptions.



Warnings are attached to a thread-local context, and are sent out when
we leave the outer-most context object. This gives us a warning that
points to the user call-site rather than somewhere buried in Rerun code.



For functions, this decorator checks for a strict kwarg and uses it to
override the global strict mode if provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| context | A string describing the context of the exception. If not provided, the function name will be used.TYPE:str\| NoneDEFAULT:None |
| depth_to_user_code | The number of frames to skip when building the warning context. This should be the number of frames between the user code and the context manager.TYPE:intDEFAULT:1 |
| exception_return_value | If an exception is caught, this value will be returned instead of the function's return value.TYPE:AnyDEFAULT:None |



#### defdeprecated_param(name,*,use_instead=None,since=None)



Marks a parameter as deprecated.



@deprecated_param(foo, use_instead="bar", since="0.23")
def foo(foo: int | None = None, bar: str | None = None) -> None:
    ...



#### defset_strict_mode(mode)



Turn strict mode on/off.



In strict mode, incorrect use of the Rerun API (wrong parameter types etc.)
will result in exception being raised.
When strict mode is off, such problems are instead logged as warnings.



The default is controlled with the `RERUN_STRICT` environment variable,
or `False` if it is not set.



#### defstrict_mode()



Strict mode enabled.



In strict mode, incorrect use of the Rerun API (wrong parameter types etc.)
will result in exception being raised.
When strict mode is on, such problems are instead logged as warnings.



The default is controlled with the `RERUN_STRICT` environment variable,
or `False` if it is not set.