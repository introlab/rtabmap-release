Name:           ros-jade-rtabmap
Version:        0.11.7
Release:        0%{?dist}
Summary:        ROS rtabmap package

Group:          Development/Libraries
License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libfreenect-devel
Requires:       libsq3-devel
Requires:       openni-devel
Requires:       pcl-devel
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-qt-gui-cpp
Requires:       vtk-qt
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  libfreenect-devel
BuildRequires:  libsq3-devel
BuildRequires:  openni-devel
BuildRequires:  pcl-devel
BuildRequires:  proj-devel
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-qt-gui-cpp
BuildRequires:  vtk-qt
BuildRequires:  zlib-devel

%description
RTAB-Map's standalone library. RTAB-Map is a RGB-D SLAM approach with real-time
constraints.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Jun 01 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.7-0
- Autogenerated by Bloom

* Sat May 14 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.11.5-0
- Autogenerated by Bloom

* Fri Mar 25 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-4
- Autogenerated by Bloom

* Thu Mar 24 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-3
- Autogenerated by Bloom

* Thu Mar 24 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-2
- Autogenerated by Bloom

* Wed Mar 23 2016 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-1
- Autogenerated by Bloom

* Sat Oct 17 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.10.10-0
- Autogenerated by Bloom

* Tue Aug 04 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.10.4-1
- Autogenerated by Bloom

* Tue Aug 04 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.10.4-0
- Autogenerated by Bloom

* Thu May 14 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.9.0-0
- Autogenerated by Bloom

* Tue May 12 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.12-1
- Autogenerated by Bloom

* Sun May 10 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.12-0
- Autogenerated by Bloom

