%define upstream_name    Tk-CursorControl
%define upstream_version 0.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Manipulate the mouse cursor programmatically
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz
Patch1:     fix-cursor-widget-demo-conflict.patch

BuildRequires: perl(Tk)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Tk::CursorControl is -NOT- a Tk::Widget. Rather, it uses Tk and
encompasses a collection of methods used to manipulate the cursor (aka
pointer) programmatically from a Tk program.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch1 -p1 -b .wdgconflict

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.400.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-3mdv2011.0
+ Revision: 556187
- rebuild for perl 5.12

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.400.0-2mdv2010.0
+ Revision: 430607
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4-7mdv2009.0
+ Revision: 258657
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2009.0
+ Revision: 246653
- rebuild
- fix spacing at top of description

* Mon Feb 04 2008 Jérôme Quelin <jquelin@mandriva.org> 0.4-4mdv2008.1
+ Revision: 162063
- fixing widget demo conflict with perl-Tk

* Sun Feb 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.4-3mdv2008.1
+ Revision: 161781
- specs cleanup
- binary package, removing noarch tag
- providing description

* Tue Jan 22 2008 Jérôme Quelin <jquelin@mandriva.org> 0.4-2mdv2008.1
+ Revision: 156527
- force 5.10.0 rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Jérôme Quelin <jquelin@mandriva.org> 0.4-1mdv2008.1
+ Revision: 110501
- import perl-Tk-CursorControl


