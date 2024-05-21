Name:           miracle-wm
Version:        0.2.1
Release:        1
Summary:        A tiling Wayland compositor based on Mir 
Group:          Desktop/WM
License:        GPL-3.0-or-later
URL:            https://github.com/mattkae/miracle-wm
Source0:        https://github.com/mattkae/miracle-wm/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(miral)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  cmake(nlohmann_json) >= 3.2.0
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  cmake(gtest)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  desktop-file-utils

%description
miracle-wm is a Wayland compositor based on Mir. It features a tiling window 
manager at its core, very much in the style of i3 and sway. The intention is 
to build a compositor that is flashier and more feature-rich than either of 
those compositors, like swayfx.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%cmake -DGTEST_INCLUDE_DIR=/usr/include/gtest/ -DGTEST_LIBRARY=/usr/lib64/libgtest.so -DGTEST_MAIN_LIBRARY=/usr/lib64/libgtest_main.so
%make_build

%install
%make_install -C build

%files
%license LICENSE
%{_bindir}/miracle-wm
%{_bindir}/miracle-wm-sensible-terminal
#{_datarootdir}/wayland-sessions/miracle-wm.desktop
