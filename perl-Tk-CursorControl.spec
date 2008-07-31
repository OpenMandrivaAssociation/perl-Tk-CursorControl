
%define realname   Tk-CursorControl
%define version    0.4
%define release    %mkrel 7

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Manipulate the mouse cursor programmatically
Source:     http://www.cpan.org/modules/by-module/Tk/%{realname}-%{version}.tar.gz
#
# Patch 1-99: Mandriva patches
Patch1:     fix-cursor-widget-demo-conflict.patch

Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Tk)

%description
Tk::CursorControl is -NOT- a Tk::Widget. Rather, it uses Tk and
encompasses a collection of methods used to manipulate the cursor (aka
pointer) programmatically from a Tk program.

%prep
%setup -q -n %{realname}-%{version} 
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



