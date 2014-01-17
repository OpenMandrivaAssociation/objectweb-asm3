
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		objectweb-asm3
Version:	3.3.1
Release:	8.0
License:	GPLv3+
Source0:	objectweb-asm3-3.3.1-8.0-omv2014.0.noarch.rpm
Source1:	objectweb-asm3-javadoc-3.3.1-8.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/objectweb-asm3
BuildArch:	noarch
Summary:	objectweb-asm3 bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	mvn(asm:asm) = 3.3.1
Provides:	mvn(asm:asm-all) = 3.3.1
Provides:	mvn(asm:asm-all-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-analysis) = 3.3.1
Provides:	mvn(asm:asm-analysis-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-commons) = 3.3.1
Provides:	mvn(asm:asm-commons-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-parent) = 3.3.1
Provides:	mvn(asm:asm-parent:pom:) = 3.3.1
Provides:	mvn(asm:asm-tree) = 3.3.1
Provides:	mvn(asm:asm-tree-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-util) = 3.3.1
Provides:	mvn(asm:asm-util-distroshaded) = 3.3.1
Provides:	mvn(asm:asm-xml) = 3.3.1
Provides:	mvn(asm:asm-xml-distroshaded) = 3.3.1
Provides:	mvn(org.eclipse.jetty.orbit:org.objectweb.asm) = 3.3.1
Provides:	objectweb-asm3 = 3.3.1-8.0:2014.0
Provides:	osgi(org.objectweb.asm) = 3.3.1

%description
objectweb-asm3 bootstrap version.

%files
/usr/bin/objectweb-asm3-processor
/usr/share/doc/objectweb-asm3
/usr/share/doc/objectweb-asm3/LICENSE.txt
/usr/share/doc/objectweb-asm3/README.txt
/usr/share/java/objectweb-asm3
/usr/share/java/objectweb-asm3/asm-all-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-all.jar
/usr/share/java/objectweb-asm3/asm-analysis-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-analysis.jar
/usr/share/java/objectweb-asm3/asm-commons-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-commons.jar
/usr/share/java/objectweb-asm3/asm-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-tree-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-tree.jar
/usr/share/java/objectweb-asm3/asm-util-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-util.jar
/usr/share/java/objectweb-asm3/asm-xml-distroshaded.jar
/usr/share/java/objectweb-asm3/asm-xml.jar
/usr/share/java/objectweb-asm3/asm.jar
/usr/share/maven-fragments/objectweb-asm3.xml
/usr/share/maven-poms/JPP.objectweb-asm3-asm-all-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-all.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-analysis-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-analysis.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-commons-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-commons.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-parent.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-tree-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-tree.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-util-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-util.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-xml-distroshaded.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm-xml.pom
/usr/share/maven-poms/JPP.objectweb-asm3-asm.pom

#------------------------------------------------------------------------
%package	-n objectweb-asm3-javadoc
Version:	3.3.1
Release:	8.0
Summary:	objectweb-asm3-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	objectweb-asm3-javadoc = 3.3.1-8.0:2014.0

%description	-n objectweb-asm3-javadoc
objectweb-asm3-javadoc bootstrap version.

%files		-n objectweb-asm3-javadoc
/usr/share/doc/objectweb-asm3-javadoc
/usr/share/doc/objectweb-asm3-javadoc/LICENSE.txt
/usr/share/javadoc/objectweb-asm3
/usr/share/javadoc/objectweb-asm3/allclasses-frame.html
/usr/share/javadoc/objectweb-asm3/allclasses-noframe.html
/usr/share/javadoc/objectweb-asm3/constant-values.html
/usr/share/javadoc/objectweb-asm3/deprecated-list.html
/usr/share/javadoc/objectweb-asm3/help-doc.html
/usr/share/javadoc/objectweb-asm3/index-all.html
/usr/share/javadoc/objectweb-asm3/index.html
/usr/share/javadoc/objectweb-asm3/org
/usr/share/javadoc/objectweb-asm3/org/objectweb
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/AnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/Attribute.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/ByteVector.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/ClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/ClassReader.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/ClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/ClassWriter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/FieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/Label.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/MethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/MethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/Opcodes.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/Type.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/AnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/Attribute.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/ByteVector.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/ClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/ClassReader.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/ClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/ClassWriter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/FieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/Label.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/MethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/MethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/Opcodes.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/class-use/Type.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/AdviceAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/AnalyzerAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/CodeSizeEvaluator.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/EmptyVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/GeneratorAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/InstructionAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/JSRInlinerAdapter.Subroutine.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/JSRInlinerAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/LocalVariablesSorter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/Method.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/Remapper.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/RemappingAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/RemappingClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/RemappingFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/RemappingMethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/RemappingSignatureAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/SerialVersionUIDAdder.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/SimpleRemapper.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/StaticInitMerger.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/TableSwitchGenerator.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/TryCatchBlockSorter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/AdviceAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/AnalyzerAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/CodeSizeEvaluator.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/EmptyVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/GeneratorAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/InstructionAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/JSRInlinerAdapter.Subroutine.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/JSRInlinerAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/LocalVariablesSorter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/Method.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/Remapper.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/RemappingAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/RemappingClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/RemappingFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/RemappingMethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/RemappingSignatureAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/SerialVersionUIDAdder.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/SimpleRemapper.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/StaticInitMerger.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/TableSwitchGenerator.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/class-use/TryCatchBlockSorter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/commons/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/SignatureReader.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/SignatureVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/SignatureWriter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/class-use/SignatureReader.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/class-use/SignatureVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/class-use/SignatureWriter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/signature/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/AbstractInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/AnnotationNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/ClassNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/FieldInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/FieldNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/FrameNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/IincInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/InnerClassNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/InsnList.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/InsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/IntInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/JumpInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/LabelNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/LdcInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/LineNumberNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/LocalVariableNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/LookupSwitchInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/MemberNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/MethodInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/MethodNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/MultiANewArrayInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/TableSwitchInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/TryCatchBlockNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/TypeInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/VarInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/Analyzer.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/AnalyzerException.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/BasicInterpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/BasicValue.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/BasicVerifier.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/Frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/Interpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/SimpleVerifier.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/SourceInterpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/SourceValue.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/Value.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/Analyzer.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/AnalyzerException.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/BasicInterpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/BasicValue.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/BasicVerifier.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/Frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/Interpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/SimpleVerifier.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/SourceInterpreter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/SourceValue.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/class-use/Value.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/analysis/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/AbstractInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/AnnotationNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/ClassNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/FieldInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/FieldNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/FrameNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/IincInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/InnerClassNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/InsnList.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/InsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/IntInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/JumpInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/LabelNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/LdcInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/LineNumberNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/LocalVariableNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/LookupSwitchInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/MemberNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/MethodInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/MethodNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/MultiANewArrayInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/TableSwitchInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/TryCatchBlockNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/TypeInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/class-use/VarInsnNode.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/tree/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifiable.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifierAbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifierAnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifierClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifierFieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/ASMifierMethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/AbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/CheckAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/CheckClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/CheckFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/CheckMethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/CheckSignatureAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceAbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceAnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceFieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceMethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/TraceSignatureVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/Traceable.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifiable.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifierAbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifierAnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifierClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifierFieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/ASMifierMethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/AbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/CheckAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/CheckClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/CheckFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/CheckMethodAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/CheckSignatureAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceAbstractVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceAnnotationVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceClassVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceFieldVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceMethodVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/TraceSignatureVisitor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/class-use/Traceable.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/util/package-use.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/ASMContentHandler.Rule.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/ASMContentHandler.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/Processor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/SAXAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/SAXAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/SAXClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/SAXCodeAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/SAXFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/asm-xml.dtd
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/ASMContentHandler.Rule.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/ASMContentHandler.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/Processor.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/SAXAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/SAXAnnotationAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/SAXClassAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/SAXCodeAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/class-use/SAXFieldAdapter.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/package-frame.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/package-summary.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/package-tree.html
/usr/share/javadoc/objectweb-asm3/org/objectweb/asm/xml/package-use.html
/usr/share/javadoc/objectweb-asm3/overview-frame.html
/usr/share/javadoc/objectweb-asm3/overview-summary.html
/usr/share/javadoc/objectweb-asm3/overview-tree.html
/usr/share/javadoc/objectweb-asm3/package-list
/usr/share/javadoc/objectweb-asm3/resources
/usr/share/javadoc/objectweb-asm3/resources/background.gif
/usr/share/javadoc/objectweb-asm3/resources/tab.gif
/usr/share/javadoc/objectweb-asm3/resources/titlebar.gif
/usr/share/javadoc/objectweb-asm3/resources/titlebar_end.gif
/usr/share/javadoc/objectweb-asm3/serialized-form.html
/usr/share/javadoc/objectweb-asm3/stylesheet.css

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
