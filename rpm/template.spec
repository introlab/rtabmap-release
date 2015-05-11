Name:           ros-indigo-rtabmap
Version:        0.8.12
Release:        0%{?dist}
Summary:        ROS rtabmap package

Group:          Development/Libraries
License:        BSD
URL:            http://introlab.github.io/rtabmap
Source0:        %{name}-%{version}.tar.gz

Requires:       libsq3-devel
Requires:       openni-devel
Requires:       pcl-devel
Requires:       qt-devel
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-libfreenect
Requires:       zlib-devel
BuildRequires:  cmake
BuildRequires:  libsq3-devel
BuildRequires:  openni-devel
BuildRequires:  pcl-devel
BuildRequires:  qt-devel
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-libfreenect
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
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun May 10 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.12-0
- Autogenerated by Bloom

* Sun Feb 08 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.3-1
- Autogenerated by Bloom

* Sun Feb 08 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.3-0
- Autogenerated by Bloom

* Mon Jan 12 2015 Mathieu Labbe <matlabbe@gmail.com> - 0.8.1-0
- Autogenerated by Bloom

* Sun Dec 14 2014 Mathieu Labbe <matlabbe@gmail.com> - 0.8.0-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Mathieu Labbe <matlabbe@gmail.com> - 0.7.3-0
- Autogenerated by Bloom

* Thu Nov 27 2014 Mathieu Labbe <matlabbe@gmail.com> - 0.7.2-0
- Autogenerated by Bloom

