+++
title = "Creating a Setup Package for a Custom SSIS Data Flow Component"
date = "2007-03-22T22:57:00Z"
tags = []
+++

## SQL Server's Pipeline Components Folder

To install an item into the special folders you need to be looking at the
_File System_ view on the setup project. If you are not already there, right
click on the setup project and select _View &gt; File System_. Once you are at
the file system view right click on _File System on Target Machine_ and select
_Add Special Folder &gt; Custom Folder_. Name the new folder something
sensible and set the _DefaultLocation_ property to `C:\Program Files\Microsoft
SQL Server\90\DTS\PipelineComponents`. Now right click on the folder and
select _Add &gt; Project Output..._ then select the project that contains the
SSIS component. You will probably see a whole bunch of detected dependencies
that you don't need to install. For each dependency that isn't needed go to
the property page and set Exclude to _True_.

## The GAC

The GAC is a special folder that windows uses to control assemblies and all
the different versions of them. To add the .dll(s) into the GAC go back to the
_File System_ view, right click on _File System on Target Machine_ and select
_Add Special Folder &gt; Global Assembly Cache Folder_. Now right click on the
_Global Assembly Cache folder_ and add the output for the project that
contains the SSIS component.

## Conclusion

This should install the assembly into both the GAC and the SSIS Pipeline
Components folder. Go forth and code!

