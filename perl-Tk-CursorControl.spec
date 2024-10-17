%define upstream_name    Tk-CursorControl
%define upstream_version 0.4

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7

Summary:    Manipulate the mouse cursor programmatically
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Tk)
BuildRequires: perl-devel

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
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
