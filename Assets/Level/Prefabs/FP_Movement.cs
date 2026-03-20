using UnityEngine;
using UnityEngine.InputSystem;

public class FP_Movement : MonoBehaviour
{
	private CharacterController controller;
	private Animator animator;
	private Vector2 moveInput, lookInput;
	private Vector3 move;
	public GameObject camera;

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        controller = GetComponent<CharacterController>();
		animator = GetComponent<Animator>();
		animator.speed = 0.0f;
    }

    // Update is called once per frame
    void Update()
    {
        controller.Move(move * Time.deltaTime);
		controller.transform.Rotate(Vector3.up, lookInput.x * Time.deltaTime);
		camera.transform.Rotate(Vector3.right, -lookInput.y * Time.deltaTime);
    }
	
	public void OnMove(InputValue value)
	{
		moveInput = value.Get<Vector2>();
		move = transform.right * moveInput.x;
		move += transform.forward * moveInput.y;
		move *= 2.0f;
		animator.speed = moveInput.y;
	}
	
	public void OnLook(InputValue value)
    {
		lookInput = value.Get<Vector2>() * 10.0f;
    }
}
