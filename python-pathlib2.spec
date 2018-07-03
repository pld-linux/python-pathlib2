%bcond_with	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pathlib2
Summary:	Object-oriented filesystem paths
Summary(pl.UTF-8):	Zorientowane obiektowo ścieżki systemu plików
Name:		python-%{module}
Version:	2.2.1
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/ab/d8/ac7489d50146f29d0a14f65545698f4545d8a6b739b24b05859942048b56/pathlib2-%{version}.tar.gz
# Source0-md5:	6c75bfde898b6c88627621a48ee8de14
URL:		https://pypi.python.org/pypi/pathlib2/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-scandir
BuildRequires:	python-setuptools
BuildRequires:	python-test
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-scandir
BuildRequires:	python3-setuptools
BuildRequires:	python3-test
%endif
Requires:	python-modules
Requires:	python-scandir
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of pathlib2 is to provide a backport of standard pathlib
module which tracks the standard library module, so all the newest
features of the standard pathlib can be used also on older Python
versions.

# %%description -l pl.UTF-8

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-scandir

%description -n python3-%{module}
The goal of pathlib2 is to provide a backport of standard pathlib
module which tracks the standard library module, so all the newest
features of the standard pathlib can be used also on older Python
versions.

# %%description -n python3-%{module} -l pl.UTF-8

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}


%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

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
%doc README.rst CHANGELOG.rst
%{py_sitescriptdir}/%{module}.py*
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst CHANGELOG.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.*.py*
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
