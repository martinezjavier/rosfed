Name:           ros-kinetic-rospy
Version:        1.12.7
Release:        1%{?dist}
Summary:        ROS package rospy

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/ros_comm-release/archive/release/kinetic/rospy/1.12.7-0.tar.gz#/ros-kinetic-rospy-1.12.7-source0.tar.gz


BuildArch: noarch

BuildRequires:  ros-kinetic-catkin

Requires:       numpy
Requires:       python-rospkg
Requires:       PyYAML
Requires:       ros-kinetic-genpy
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-rosgraph_msgs
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-std_msgs

%description
rospy is a pure Python client library for ROS. The rospy client API
enables Python programmers to quickly interface with ROS


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
  --pkg rospy

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
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.7-1
- Update auto-generated Spec file
