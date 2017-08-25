Name:           ros-kinetic-camera_info_manager
Version:        1.11.12
Release:        2%{?dist}
Summary:        ROS package camera_info_manager

License:        BSD
URL:            http://ros.org/wiki/camera_info_manager

Source0:        https://github.com/ros-gbp/image_common-release/archive/release/kinetic/camera_info_manager/1.11.12-0.tar.gz#/ros-kinetic-camera_info_manager-1.11.12-source0.tar.gz



BuildRequires:  boost-devel
BuildRequires:  gtest-devel
BuildRequires:  ros-kinetic-camera_calibration_parsers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-image_transport
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor_msgs

Requires:       ros-kinetic-camera_calibration_parsers
Requires:       ros-kinetic-image_transport
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-sensor_msgs

%description
This package provides a C++ interface for camera calibration
information. It provides CameraInfo, and handles SetCameraInfo service
requests, saving and restoring the camera calibration data.


%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \


source %{_libdir}/ros/setup.bash

DESTDIR=%{buildroot} ; export DESTDIR

catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg camera_info_manager

rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,setup*,env.sh}

find %{buildroot}/%{_libdir}/ros/{bin,etc,include,lib/pkgconfig,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list


find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list

%files -f files.list



%changelog
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.11.12-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.11.12-1
- Update auto-generated Spec file