Name:           ros-kinetic-bondcpp
Version:        1.7.19
Release:        1%{?dist}
Summary:        ROS package bondcpp

License:        BSD
URL:            http://www.ros.org/wiki/bondcpp

Source0:        https://github.com/ros-gbp/bond_core-release/archive/release/kinetic/bondcpp/1.7.19-0.tar.gz#/ros-kinetic-bondcpp-1.7.19-source0.tar.gz



BuildRequires:  boost-devel
BuildRequires:  libuuid-devel
BuildRequires:  ros-kinetic-bond
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake_modules
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-smclib

Requires:       boost-devel
Requires:       libuuid-devel
Requires:       ros-kinetic-bond
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-smclib

%description
C++ implementation of bond, a mechanism for checking when another
process has terminated.


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
  --pkg bondcpp

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
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.7.19-1
- Update auto-generated Spec file
