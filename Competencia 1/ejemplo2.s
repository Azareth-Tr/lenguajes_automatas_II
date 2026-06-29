	.file	"ejemplo2.c"
	.text
	.globl	cicloWhile
	.def	cicloWhile;	.scl	2;	.type	32;	.endef
	.seh_proc	cicloWhile
cicloWhile:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$16, %rsp
	.seh_stackalloc	16
	.seh_endprologue
	movl	$10, -4(%rbp)
	jmp	.L2
.L3:
	subl	$1, -4(%rbp)
.L2:
	cmpl	$0, -4(%rbp)
	jg	.L3
	movl	$0, %eax
	addq	$16, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (Rev5, Built by MSYS2 project) 16.1.0"
