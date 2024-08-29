Name:           miracle-wm
Version:        0.3.4
Release:        1
Summary:        A tiling Wayland compositor based on Mir 
Group:          Desktop/WM
License:        GPL-3.0-or-later
URL:            https://github.com/mattkae/miracle-wm
Source0:        https://github.com/mattkae/miracle-wm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(miral)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  desktop-file-utils
BuildRequires:	gtest-devel

BuildSystem:  cmake
BuildOption:  -DGTEST_INCLUDE_DIR=/usr/include/gtest/ 
BuildOption:  -DGTEST_LIBRARY=/usr/lib64/libgtest.so 
BuildOption:  -DGTEST_MAIN_LIBRARY=/usr/lib64/libgtest_main.so

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling window 
manager at its core, very much in the style of i3 and sway. The intention is 
to build a compositor that is flashier and more feature-rich than either of 
those compositors, like swayfx.

%prep -a
# Don't force gcc -- especially not while its LTO is broken and clang's works
sed -i -e 's,^set(CMAKE_CXX_COMPILER,# set(CMAKE_CXX_COMPILER,' CMakeLists.txt tests/CMakeLists.txt

%files
%license LICENSE
%{_bindir}/miracle-wm
%{_bindir}/miracle-wm-sensible-terminal
%{_datadir}/wayland-sessions/miracle-wm.desktop
