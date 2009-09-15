%define 	module	application
Summary:	Basic building blocks for python applications
Name:		python-%{module}
Version:	1.1.5
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/python-application/%{name}-%{version}.tar.gz
# Source0-md5:	d43399becc6b2850a2ea80a34375781b
URL:		http://pypi.python.org/pypi/python-application
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a collection of modules that are useful when building python
applications. Their purpose is to eliminate the need to divert resources into
implementing the small tasks that every application needs to do in order to
run successfully and focus instead on the application logic itself.

The modules that the application package provides are:

1. process       - UNIX process and signal management.
2. python        - python utility classes and functions.
3. configuration - a simple interface to handle configuration files.
4. log           - an extensible system logger for console and syslog.
5. debug         - memory troubleshooting and execution timing.
6. system        - interaction with the underlying operating system.
7. notification  - an application wide notification system.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/configuration
%{py_sitescriptdir}/%{module}/configuration/*.py[co]
%dir %{py_sitescriptdir}/%{module}/debug
%{py_sitescriptdir}/%{module}/debug/*.py[co]
%dir %{py_sitescriptdir}/%{module}/python
%{py_sitescriptdir}/%{module}/python/*.py[co]
%{py_sitescriptdir}/*-*.egg-info
