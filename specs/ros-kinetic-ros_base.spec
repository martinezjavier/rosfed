Name:           ros-kinetic-ros_base
Version:        1.3.1
Release:        1%{?dist}
Summary:        ROS package ros_base

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/metapackages-release/archive/release/kinetic/ros_base/1.3.1-0.tar.gz#/ros-kinetic-ros_base-1.3.1-source0.tar.gz


BuildArch: noarch

BuildRequires:  ros-kinetic-catkin

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-bond_core
Requires:       ros-kinetic-class_loader
Requires:       ros-kinetic-dynamic_reconfigure
Requires:       ros-kinetic-nodelet_core
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-ros_core

%description
A metapackage which extends ros_core and includes other basic non-
robot tools like actionlib, dynamic reconfigure, nodelets, and
pluginlib.


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
  --pkg ros_base

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
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.1-1
- Update auto-generated Spec file
