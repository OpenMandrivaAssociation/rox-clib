%define name rox-clib
%define oname ROX-CLib
%define version 2.1.7
%define release %mkrel 3
%define major 6
%define libname %mklibname rox-c %major

Summary: Shared code for ROX applications
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.kerofin.demon.co.uk/rox/%{oname}-%{version}.tar.bz2
URL: http://www.kerofin.demon.co.uk/rox/libs.html#rox-clib2
License: GPL
Group: Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libgtk+2.0-devel
BuildRequires: libxml2-devel
Requires: rox

%description
A library for ROX applications written in C.

This is version 1.1, a development version leading up to 2.0 which will be
for GTK+ 2.x.

%package -n %libname
Group: System/Libraries
Summary: Shared library of ROX-Clib
Requires: %name >= %version

%description -n %libname
A library for ROX applications written in C.

This is version 1.1, a development version leading up to 2.0 which will be
for GTK+ 2.x.


%package -n %libname-devel
Group: Development/C
Summary: Headers for the rox C library
Requires: %libname = %version
Provides: librox-c-devel = %version-%release
Requires: libgtk+2.0-devel
Requires: libxml2-devel

%description -n %libname-devel
A library for ROX applications written in C.

This is version 1.1, a development version leading up to 2.0 which will be
for GTK+ 2.x.


%prep
%setup -q -n %oname
rm -rf .xvpics

%build
export CFLAGS="%optflags"
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_libdir
cd ..
cp -r %oname %buildroot/%_libdir
rm -rf %buildroot/%_libdir/%oname/src
perl -pi -e "s/lib/%_lib/g" %buildroot/%_libdir/%oname/Linux-*/bin/rox_run
perl -pi -e "s!$RPM_BUILD_DIR/%oname/src/../!%_libdir/%oname/!"  %buildroot/%_libdir/%oname/Linux-*/lib/librox-clib.la 

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %_libdir/%oname/Help
%dir %_libdir/%oname
%_libdir/%oname/ROX-CLib.xml
%_libdir/%oname/App*
%_libdir/%oname/.DirIcon
%dir %_libdir/%oname/Linux*/
%_libdir/%oname/Linux*/bin
%dir %_libdir/%oname/Linux*/lib

%files -n %libname
%defattr(-,root,root)
%_libdir/%oname/Linux*/lib/librox-clib.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/%oname/Linux*/lib/librox-clib.a
%_libdir/%oname/Linux*/lib/librox-clib.so
%_libdir/%oname/Linux*/lib/librox-clib.la
%_libdir/%oname/Linux*/lib/ROX-CLib.pc
%_libdir/%oname/Linux*/include


