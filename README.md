List Longest Paths
===================

Overview
--------

This script recursively traverse a given directory and identify which filepath are greater than a given length.

This is particularly useful when trying to identitify which files living in a windows source or build tree are causing trouble due to the [Maximum Path Length Limitation][maxpath-length-limit].

Usage
-----

```
$ ./list_longest_paths.py -h
Usage: list_longest_paths.py [options] <directory>

Options:
  -h, --help            show this help message and exit
  -l MINIMUM_LENGTH, --minimum-length=MINIMUM_LENGTH
                        specify minimum length to consider when listing the
                        longest paths
  -v, --verbose         Print verbose information
  --extra-verbose       Print extra verbose information
```

By default `MINIMUM_LENGTH` is `259` (`MAX_PATH -1`) . See [Maximum Path Length Limitation][maxpath-length-limit].


```
$ ./list_longest_paths.py ~/Projects/Slicer-AHM-Superbuild-Debug/
[262] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/CMakeFiles/CTKVisualizationVTKWidgetsPythonQt.dir/generated_cpp/org_commontk_CTKVisualizationVTKWidgets/org_commontk_CTKVisualizationVTKWidgets_module_init.cpp.o
[281] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/Slicer-build/Modules/Loadable/EMSegment/Qt/Widgets/CMakeFiles/qSlicerEMSegmentModuleWidgetsPythonQt.dir/generated_cpp/org_slicer_module_qSlicerEMSegmentModuleWidgets/org_slicer_module_qSlicerEMSegmentModuleWidgets_module_init.cpp.o
[277] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/Slicer-build/Modules/Loadable/EMSegment/Qt/Widgets/CMakeFiles/qSlicerEMSegmentModuleWidgetsPythonQt.dir/generated_cpp/org_slicer_module_qSlicerEMSegmentModuleWidgets/moc_org_slicer_module_qSlicerEMSegmentModuleWidgets_all.cpp.o
[274] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/Slicer-build/Modules/Loadable/EMSegment/Qt/Widgets/CMakeFiles/qSlicerEMSegmentModuleWidgetsPythonQt.dir/generated_cpp/org_slicer_module_qSlicerEMSegmentModuleWidgets/org_slicer_module_qSlicerEMSegmentModuleWidgets_init.cpp.o
[...]
```

Simple.

Note also that passing the `--verbose` options will provide you with more details:

```
$ ./list_longest_paths.py -v -l 300 ~/Projects/Slicer-AHM-Superbuild-Debug/
[318] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/Slicer-build/Modules/Loadable/TractographyDisplay/Widgets/CMakeFiles/qSlicerTractographyDisplayModuleWidgetsPythonQt.dir/generated_cpp/org_slicer_module_qSlicerTractographyDisplayModuleWidgets/org_slicer_module_qSlicerTractographyDisplayModuleWidgets_module_init.cpp.o
[302] /home/jchris/Projects/Slicer-AHM-Superbuild-Debug/Slicer-build/Modules/Loadable/VolumeRendering/Widgets/CMakeFiles/qSlicerVolumeRenderingModuleWidgetsPythonQt.dir/generated_cpp/org_slicer_module_qSlicerVolumeRenderingModuleWidgets/org_slicer_module_qSlicerVolumeRenderingModuleWidgets_module_init.cpp.o

Analysis summary
	Found 2 files having length >= 300 by recursively traversing directory [/home/jchris/Projects/Slicer-AHM-Superbuild-Debug/]
	Number of checked paths is 85966
```


Installation
------------

[Download the script](https://raw.github.com/jcfr/list-longest-paths/master/list_longest_paths.py).


Contributing
------------

Once you've made your great commits:

1. [Fork][fk] list-longest-paths
2. Create a topic branch - `git checkout -b my_branch`
3. Push to your branch - `git push origin my_branch`
4. Submit a [Pull Request][pr]
5. That's it!


Meta
----

* Code: `git clone git://github.com/jcfr/list-longest-paths.git`
* Home: <http://jcfr.github.com>
* Bugs: <http://github.com/jcfr/list-longest-paths/issues>

License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

[fk]: http://help.github.com/forking/
[pr]: https://help.github.com/articles/using-pull-requests
[maxpath-length-limit]: http://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx#maxpath

