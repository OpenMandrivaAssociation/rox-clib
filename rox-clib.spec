%define oname ROX-CLib
%define major 6
%define libname %mklibname rox-c %major
%define develname %mklibname -d rox-c

Summary:	Shared code for ROX applications
Name:		rox-clib
Version:	2.1.10
Release:	3
Source0:	http://www.kerofin.demon.co.uk/rox/%{oname}-%{version}.tar.gz
URL:		http://www.kerofin.demon.co.uk/rox/ROX-CLib.html
License:	GPLv2
Group:		Graphical desktop/Other
BuildRequires:	libgtk+2.0-devel
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
export CFLAGS="%optflags"
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




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.10-2mdv2011.0
+ Revision: 614711
- the mass rebuild of 2010.1 packages

* Thu Mar 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.1.10-1mdv2010.1
+ Revision: 514332
- fix license
- fix file list
- update to 2.1.10

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.1.9-4mdv2010.0
+ Revision: 433356
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1.9-3mdv2009.0
+ Revision: 242555
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix description

* Wed Sep 05 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.9-1mdv2008.0
+ Revision: 79945
- new version
- new devel name
- update file list


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.7-3mdv2007.0
+ Revision: 108622
- Import rox-clib

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.1.7-3mdv2007.1
- fix devel deps

* Fri Jul 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.7-2mdk
- Rebuild

* Mon Jan 02 2006 Götz Waschk <waschk@mandriva.org> 2.1.7-1mdk
- new major
- New release 2.1.7
- use mkrel

* Tue Oct 18 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.1.5-1mdk
- New release 2.1.5

* Wed Nov 24 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.1.4-1mdk
- New release 2.1.4

* Mon Sep 27 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.1.3-1mdk
- New release 2.1.3

* Sat Aug 07 2004 Götz Waschk <waschk@linux-mandrake.com> 2.1.2-1mdk
- add missing file
- New release 2.1.2

* Sat May 15 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.1.1-1mdk
- New release 2.1.1

* Thu May 06 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.1.0-1mdk
- New release 2.1.0

* Sat Jan 17 2004 Götz Waschk <waschk@linux-mandrake.com> 2.0.0-1mdk
- new version

