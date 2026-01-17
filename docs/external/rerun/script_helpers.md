---
source: https://ref.rerun.io/docs/python/stable/common/script_helpers
title: Script Helpers
---

# Script Helpers



### rerun



#### defscript_add_args(parser)



Add common Rerun script arguments to `parser`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| parser | The parser to add arguments to.TYPE:ArgumentParser |



#### defscript_setup(args,application_id,*,recording_id=None,default_blueprint=None)



Run common Rerun script setup actions. Connect to the viewer if necessary.



| PARAMETER | DESCRIPTION |
| --- | --- |
| args | The parsed arguments fromparser.parse_args().TYPE:Namespace |
| application_id | The application ID to use for the viewer.TYPE:str |
| recording_id | Set the recording ID that this process is logging to, as a UUIDv4.The default recording_id is based onmultiprocessing.current_process().authkeywhich means that all processes spawned withmultiprocessingwill have the same default recording_id.If you are not usingmultiprocessingand still want several different Python processes to log to the same Rerun instance (and be part of the same recording), you will need to manually assign them all the same recording_id. Any random UUIDv4 will work, or copy the recording id for the parent process.TYPE:Optional[str]DEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



#### defscript_teardown(args)



Run common post-actions. Sleep if serving the web viewer.



| PARAMETER | DESCRIPTION |
| --- | --- |
| args | The parsed arguments fromparser.parse_args().TYPE:Namespace |