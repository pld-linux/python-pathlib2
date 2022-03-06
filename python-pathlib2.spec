#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pathlib2
Summary:	Object-oriented filesystem paths
Summary(pl.UTF-8):	Zorientowane obiektowo ścieżki systemu plików
Name:		python-%{module}
Version:	2.3.7.post1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathlib2/
Source0:	https://files.pythonhosted.org/packages/source/p/pathlib2/pathlib2-%{version}.tar.gz
# Source0-md5:	a8a4d8f897e709006a4586cf2102edc6
URL:		https://pypi.org/project/pathlib2/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-scandir
BuildRequires:	python-six
BuildRequires:	python-test >= 1:2.6
BuildRequires:	python-typing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
BuildRequires:	python3-test >= 1:3.5
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of pathlib2 is to provide a backport of standard pathlib
module which tracks the standard library module, so all the newest
features of the standard pathlib can be used also on older Python
versions.

%description -l pl.UTF-8
Celem pathlib2 jest udostępnienie backportu modułu standardowego
pathlib podążającego za modułem biblioteki standardowej, aby
wszystkie najnowsze możliwości standardowego pathlib mogły być
używane także ze starszymi wersjami Pythona.

%package -n python3-%{module}
Summary:	Object-oriented filesystem paths
Summary(pl.UTF-8):	Zorientowane obiektowo ścieżki systemu plików
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
The goal of pathlib2 is to provide a backport of standard pathlib
module which tracks the standard library module, so all the newest
features of the standard pathlib can be used also on older Python
versions.

%description -n python3-%{module} -l pl.UTF-8
Celem pathlib2 jest udostępnienie backportu modułu standardowego
pathlib podążającego za modułem biblioteki standardowej, aby
wszystkie najnowsze możliwości standardowego pathlib mogły być
używane także ze starszymi wersjami Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.rst README.rst
%{py_sitescriptdir}/pathlib2
%{py_sitescriptdir}/pathlib2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.rst README.rst
%{py3_sitescriptdir}/pathlib2
%{py3_sitescriptdir}/pathlib2-%{version}-py*.egg-info
%endif
