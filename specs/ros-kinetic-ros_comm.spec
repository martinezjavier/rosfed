Name:           ros-kinetic-ros_comm
Version:        1.12.7
Release:        2%{?dist}
Summary:        ROS package ros_comm

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/ros_comm-release/archive/release/kinetic/ros_comm/1.12.7-0.tar.gz#/ros-kinetic-ros_comm-1.12.7-source0.tar.gz


BuildArch: noarch

BuildRequires:  ros-kinetic-catkin

Requires:       ros-kinetic-message_filters
Requires:       ros-kinetic-ros
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-rosgraph_msgs
Requires:       ros-kinetic-roslaunch
Requires:       ros-kinetic-roslisp
Requires:       ros-kinetic-rosmaster
Requires:       ros-kinetic-rosmsg
Requires:       ros-kinetic-rosnode
Requires:       ros-kinetic-rosout
Requires:       ros-kinetic-rosparam
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rosservice
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-roswtf
Requires:       ros-kinetic-std_srvs
Requires:       ros-kinetic-topic_tools
Requires:       ros-kinetic-xmlrpcpp

%description
ROS communications-related packages, including core client libraries
(roscpp, rospy) and graph introspection tools (rostopic, rosnode,
rosservice, rosparam).


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
  --pkg ros_comm

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
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.7-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.7-1
- Update auto-generated Spec file
