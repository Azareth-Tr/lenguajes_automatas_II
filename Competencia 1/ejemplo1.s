	.file	"ejemplo1.c"
	.text
	.globl	multiplicacion
	.def	multiplicacion;	.scl	2;	.type	32;	.endef
	.seh_proc	multiplicacion
multiplicacion:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movl	%ecx, 16(%rbp)
	movl	%edx, 24(%rbp)
	movl	16(%rbp), %eax
	imull	24(%rbp), %eax
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (Rev5, Built by MSYS2 project) 16.1.0"
