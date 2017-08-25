Name:           ros-kinetic-image_view
Version:        1.12.20
Release:        2%{?dist}
Summary:        ROS package image_view

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/image_pipeline-release/archive/release/kinetic/image_view/1.12.20-0.tar.gz#/ros-kinetic-image_view-1.12.20-source0.tar.gz



BuildRequires:  gtk2-devel
BuildRequires:  ros-kinetic-camera_calibration_parsers
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cv_bridge
BuildRequires:  ros-kinetic-dynamic_reconfigure
BuildRequires:  ros-kinetic-image_transport
BuildRequires:  ros-kinetic-message_filters
BuildRequires:  ros-kinetic-message_generation
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor_msgs
BuildRequires:  ros-kinetic-std_srvs
BuildRequires:  ros-kinetic-stereo_msgs

Requires:       ros-kinetic-camera_calibration_parsers
Requires:       ros-kinetic-cv_bridge
Requires:       ros-kinetic-dynamic_reconfigure
Requires:       ros-kinetic-image_transport
Requires:       ros-kinetic-message_filters
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std_srvs

%description
A simple viewer for ROS image topics. Includes a specialized viewer
for stereo + disparity images.


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
  --pkg image_view

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
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.20-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.20-1
- Update auto-generated Spec file
