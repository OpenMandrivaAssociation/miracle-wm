#define _disable_lto 1
%define libname %mklibname miracle-wm
%define devname %mklibname -d miracle-wm

Name:           miracle-wm
Version:        0.6.2
Release:        1
Summary:        A tiling Wayland compositor based on Mir 
Group:          Desktop/WM
License:        GPL-3.0-or-later
URL:            https://github.com/mattkae/miracle-wm
Source0:        https://github.com/mattkae/miracle-wm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(miral)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  desktop-file-utils
BuildRequires:  boost-devel
BuildRequires:  %{_lib}boost-core-devel
BuildRequires:	gtest-devel
Requires: %{libname} = %{EVRD}

BuildSystem:  cmake
BuildOption:  -DGTEST_INCLUDE_DIR=/usr/include/gtest/ 
BuildOption:  -DGTEST_LIBRARY=/usr/lib64/libgtest.so 
BuildOption:  -DGTEST_MAIN_LIBRARY=/usr/lib64/libgtest_main.so

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling window 
manager at its core, very much in the style of i3 and sway. The intention is 
to build a compositor that is flashier and more feature-rich than either of 
those compositors, like swayfx.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary: Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires: %{name} = %{EVRD}
Provides: %{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.


%prep -a
# Don't force gcc -- especially not while its LTO is broken and clang's works
#sed -i -e 's,^set(CMAKE_CXX_COMPILER,# set(CMAKE_CXX_COMPILER,' CMakeLists.txt tests/CMakeLists.txt

%install -a
rm -rf %{buildroot}//usr/include/gtest/
rm -rf %{buildroot}/usr/include/gmock/
rm -rf %{buildroot}/usr/lib64/cmake/GTest/
rm -rf %{buildroot}/usr/lib64/libgmock*
rm -rf %{buildroot}/usr/lib64/libgtest*
rm -rf %{buildroot}/usr/lib64/pkgconfig/gmock*
rm -rf %{buildroot}/usr/lib64/pkgconfig/gtest*


%files
%license LICENSE
%{_bindir}/miracle-wm
%{_bindir}/miracle-wm-sensible-terminal
%{_bindir}/miracle-wm-session
%{_bindir}/miraclemsg
%{_datadir}/wayland-sessions/miracle-wm.desktop

%files -n %{libname}
%{_libdir}/libmiracle-wm-config.so.0*

%files -n %{devname}
%{_libdir}/libmiracle-wm-config.so
%{_includedir}/miracle/
%{_libdir}/pkgconfig/miracle-wm-config.pc
