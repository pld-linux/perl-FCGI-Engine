#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	FCGI
%define	pnam	Engine
Summary:	FCGI::Engine - A flexible engine for running FCGI-based applications
Name:		perl-FCGI-Engine
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	300e3e69152ca2dbdb98d07e761e7f5d
URL:		http://search.cpan.org/dist/FCGI-Engine/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Declare::Constraints::Simple)
BuildRequires:	perl(MooseX::Daemonize) >= 0.06
BuildRequires:	perl(MooseX::Getopt) >= 0.14
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl-CGI-Simple
BuildRequires:	perl-Config-Any
BuildRequires:	perl-FCGI
BuildRequires:	perl-Moose >= 0.32
BuildRequires:	perl-MooseX-AttributeHelpers >= 0.06
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-WWW-Mechanize
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module helps manage FCGI based web applications by providing a
wrapper which handles most of the low-level FCGI details for you. It
can run FCGI programs as simple scripts or as full standalone socket
based servers who are managed by FCGI::Engine::ProcManager.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/FCGI/*.pm
%{perl_vendorlib}/FCGI/Engine
%{perl_vendorlib}/Plack/Handler/FCGI
%{perl_vendorlib}/Plack/Server/FCGI
%{_mandir}/man3/*
