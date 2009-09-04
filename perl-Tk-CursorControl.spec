%define upstream_name    Tk-CursorControl
%define upstream_version 0.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

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
