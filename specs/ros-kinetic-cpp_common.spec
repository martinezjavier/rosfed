Name:           ros-kinetic-cpp_common
Version:        0.6.2
Release:        1%{?dist}
Summary:        ROS package cpp_common

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/roscpp_core-release/archive/release/kinetic/cpp_common/0.6.2-0.tar.gz#/ros-kinetic-cpp_common-0.6.2-source0.tar.gz



BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  ros-kinetic-catkin

Requires:       boost-devel
Requires:       console-bridge-devel

%description
cpp_common contains C++ code for doing things that are not necessarily
ROS related, but are useful for multiple packages. This includes
things like the ROS_DEPRECATED and ROS_FORCE_INLINE macros, as well as
code for getting backtraces. This package is a component of


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
  --pkg cpp_common

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
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 0.6.2-1
- Update auto-generated Spec file
