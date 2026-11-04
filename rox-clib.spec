%define oname ROX-CLib
%define major 6
%define libname %mklibname rox-c %major
%define develname %mklibname -d rox-c

Summary:	Shared code for ROX applications
Name:		rox-clib
Version:	2.1.10
Release:	7
Source0:	http://www.kerofin.demon.co.uk/rox/%{oname}-%{version}.tar.gz
URL:		https://www.kerofin.demon.co.uk/rox/ROX-CLib.html
License:	GPLv2
Group:		Graphical desktop/Other
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
Requires:	rox

%description
A library for ROX applications written in C.

%package -n %libname
Group: System/Libraries
Summary: Shared library of ROX-Clib
Requires: %name >= %version

%description -n %libname
A library for ROX applications written in C.

%package -n %develname
Group: Development/C
Summary: Headers for the rox C library
Requires: %libname = %version
Provides: librox-c-devel = %{EVRD}
Requires: libgtk+2.0-devel
Requires: libxml2-devel
Obsoletes: %mklibname -d rox-c 6

%description -n %develname
A library for ROX applications written in C.

%prep
%setup -q -n %oname
rm -rf .xvpics

%build
export CFLAGS="%optflags" LDFLAGS="-ldl"
./AppRun --compile

%install
mkdir -p %buildroot/%_libdir
cd ..
cp -r %oname %buildroot/%_libdir
rm -rf %buildroot/%_libdir/%oname/src
perl -pi -e "s/lib/%_lib/g" %buildroot/%_libdir/%oname/Linux-*/bin/rox_run
perl -pi -e "s!$RPM_BUILD_DIR/%oname/src/../!%_libdir/%oname/!"  %buildroot/%_libdir/%oname/Linux-*/lib/librox-clib.la 

%files
%doc %_libdir/%oname/Help
%dir %_libdir/%oname
%_libdir/%oname/ROX-CLib.xml
%_libdir/%oname/ROX-CLib-src.xml
%_libdir/%oname/App*
%_libdir/%oname/.DirIcon
%dir %_libdir/%oname/Linux*/
%_libdir/%oname/Linux*/bin
%dir %_libdir/%oname/Linux*/lib

%files -n %libname
%_libdir/%oname/Linux*/lib/librox-clib.so.%{major}*

%files -n %develname
%_libdir/%oname/Linux*/lib/librox-clib.a
%_libdir/%oname/Linux*/lib/librox-clib.so
%_libdir/%oname/Linux*/lib/ROX-CLib.pc
%_libdir/%oname/Linux*/include
