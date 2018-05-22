Name:           ros-kinetic-depth_image_proc
Version:        1.12.23
Release:        3%{?dist}
Summary:        ROS package depth_image_proc

License:        BSD
URL:            http://www.ros.org/

Source0:        https://github.com/ros-gbp/image_pipeline-release/archive/release/kinetic/depth_image_proc/1.12.23-0.tar.gz#/ros-kinetic-depth_image_proc-1.12.23-source0.tar.gz



# common BRs
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  gtest-devel
BuildRequires:  log4cxx-devel
BuildRequires:  python2-devel

BuildRequires:  boost-devel
BuildRequires:  eigen3-devel
BuildRequires:  libuuid-devel
BuildRequires:  opencv-devel
BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  ros-kinetic-catkin-devel
BuildRequires:  ros-kinetic-cmake_modules-devel
BuildRequires:  ros-kinetic-cv_bridge-devel
BuildRequires:  ros-kinetic-eigen_conversions-devel
BuildRequires:  ros-kinetic-image_geometry-devel
BuildRequires:  ros-kinetic-image_transport-devel
BuildRequires:  ros-kinetic-message_filters-devel
BuildRequires:  ros-kinetic-nodelet-devel
BuildRequires:  ros-kinetic-rostest-devel
BuildRequires:  ros-kinetic-sensor_msgs-devel
BuildRequires:  ros-kinetic-stereo_msgs-devel
BuildRequires:  ros-kinetic-tf2-devel
BuildRequires:  ros-kinetic-tf2_ros-devel

Requires:       ros-kinetic-cv_bridge
Requires:       ros-kinetic-eigen_conversions
Requires:       ros-kinetic-image_geometry
Requires:       ros-kinetic-image_transport
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-tf2_ros


%description
Contains nodelets for processing depth images such as those produced
by OpenNI camera. Functions include creating disparity images and
point clouds, as well as registering (reprojecting) a depth image into
another camera frame.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ros-kinetic-catkin-devel
Requires:       boost-devel
Requires:       eigen3-devel
Requires:       libuuid-devel
Requires:       opencv-devel
Requires:       poco-devel
Requires:       tinyxml-devel
Requires:       tinyxml2-devel
Requires:       ros-kinetic-cmake_modules-devel
Requires:       ros-kinetic-cv_bridge-devel
Requires:       ros-kinetic-eigen_conversions-devel
Requires:       ros-kinetic-image_geometry-devel
Requires:       ros-kinetic-image_transport-devel
Requires:       ros-kinetic-message_filters-devel
Requires:       ros-kinetic-nodelet-devel
Requires:       ros-kinetic-rostest-devel
Requires:       ros-kinetic-sensor_msgs-devel
Requires:       ros-kinetic-stereo_msgs-devel
Requires:       ros-kinetic-tf2-devel
Requires:       ros-kinetic-tf2_ros-devel

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.



%prep

%setup -c -T
tar --strip-components=1 -xf %{SOURCE0}

%build
# nothing to do here


%install

PYTHONUNBUFFERED=1 ; export PYTHONUNBUFFERED

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ; \
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ; \
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;} \

source %{_libdir}/ros/setup.bash

DESTDIR=%{buildroot} ; export DESTDIR


catkin_make_isolated \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATKIN_ENABLE_TESTING=OFF \
  --source . \
  --install \
  --install-space %{_libdir}/ros/ \
  --pkg depth_image_proc




rm -rf %{buildroot}/%{_libdir}/ros/{.catkin,.rosinstall,_setup*,setup*,env.sh}

touch files.list
find %{buildroot}/%{_libdir}/ros/{bin,etc,lib64/python*,lib/python*/site-packages,share} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files.list
find %{buildroot}/%{_libdir}/ros/lib*/ -mindepth 1 -maxdepth 1 \
  ! -name pkgconfig ! -name "python*" \
  | sed "s:%{buildroot}/::" >> files.list

touch files_devel.list
find %{buildroot}/%{_libdir}/ros/{include,lib*/pkgconfig} \
  -mindepth 1 -maxdepth 1 | sed "s:%{buildroot}/::" > files_devel.list

find . -maxdepth 1 -type f -iname "*readme*" | sed "s:^:%%doc :" >> files.list
find . -maxdepth 1 -type f -iname "*license*" | sed "s:^:%%license :" >> files.list


echo "This is a package automatically generated with rosfed." >> README_FEDORA
echo "See https://pagure.io/ros for more information." >> README_FEDORA
install -p -D -t %{buildroot}/%{_docdir}/%{name} README_FEDORA
echo %{_docdir}/%{name} >> files.list
install -p -D -t %{buildroot}/%{_docdir}/%{name}-devel README_FEDORA
echo %{_docdir}/%{name}-devel >> files_devel.list


%files -f files.list
%files devel -f files_devel.list


%changelog
* Tue May 22 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.23-3
- devel also requires: the devel package of each run dependency
* Tue May 22 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.23-2
- devel also requires: the devel package of each run dependency
* Tue May 15 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.23-1
- Also add upstream's exec_depend as Requires:
* Tue Feb 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.22-5
- Replace Recommends: with Requires: in devel subpackage
* Tue Feb 20 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.22-4
- Fix Requires: in devel subpackage
* Mon Feb 19 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.22-3
- Add Recommends: for all BRs to the devel subpackage
* Tue Feb 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.22-2
- Split devel package
* Tue Feb 06 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.12.22-1
- Split devel package
* Thu Nov 23 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.12.21-2
- Build against system opencv3 instead of ros-kinetic-opencv
* Sun Nov 19 2017 Till Hofmann <thofmann@fedoraproject.org> - 1.12.21-1
- Update to latest release
* Fri Aug 25 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.20-2
- Remove all Requires: on devel packages
* Wed Aug 16 2017 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.12.20-1
- Update auto-generated Spec file
